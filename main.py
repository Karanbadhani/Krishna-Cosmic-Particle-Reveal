"""Original particle-reveal animation created for Karan Badhani's portfolio."""

from dataclasses import dataclass
from pathlib import Path
import math
import random

import pygame


WINDOW_SIZE = (900, 900)
FPS = 60
BACKGROUND = (2, 7, 20)
IMAGE_NAME = "Lord_Krishna.png"

MAX_IMAGE_SIZE = (650, 790)
MAX_PARTICLES = 8500
REVEAL_AT = 5.0
REVEAL_SECONDS = 1.5


def clamp(value, minimum=0.0, maximum=1.0):
    return max(minimum, min(maximum, value))


def smoothstep(value):
    value = clamp(value)
    return value * value * (3.0 - 2.0 * value)


@dataclass
class Particle:
    start: pygame.Vector2
    target: pygame.Vector2
    colour: tuple[int, int, int]
    radius: int
    delay: float
    travel_time: float
    phase: float

    def position_at(self, elapsed):
        progress = (elapsed - self.delay) / self.travel_time

        if progress <= 0:
            return None

        eased = smoothstep(progress)
        position = self.start.lerp(self.target, eased)

        # A shrinking curve gives every particle a gentle swirling path.
        curve = (1.0 - eased) * 45.0
        position.x += math.cos(self.phase + eased * 7.0) * curve
        position.y += math.sin(self.phase + eased * 7.0) * curve

        return position, eased


class KrishnaParticleApp:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Krishna Cosmic Particle Reveal")
        self.clock = pygame.time.Clock()
        self.glow_layer = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)

        self.image = self._load_image()
        self.image_rect = self.image.get_rect(center=self.screen.get_rect().center)
        self.stars = self._create_stars(120)
        self.particles = self._create_particles()
        self.elapsed = 0.0

    def _load_image(self):
        image_path = Path(__file__).resolve().parent / IMAGE_NAME

        if not image_path.exists():
            raise FileNotFoundError(
                f"{IMAGE_NAME} was not found. Keep it beside main.py."
            )

        image = pygame.image.load(str(image_path)).convert_alpha()
        width, height = image.get_size()

        scale = min(
            MAX_IMAGE_SIZE[0] / width,
            MAX_IMAGE_SIZE[1] / height,
            1.0,
        )

        final_size = (max(1, int(width * scale)), max(1, int(height * scale)))
        return pygame.transform.smoothscale(image, final_size)

    @staticmethod
    def _create_stars(amount):
        generator = random.Random(24)
        return [
            (
                generator.randrange(WINDOW_SIZE[0]),
                generator.randrange(WINDOW_SIZE[1]),
                generator.choice((1, 1, 1, 2)),
                generator.randrange(70, 180),
            )
            for _ in range(amount)
        ]

    def _create_particles(self):
        image_width, image_height = self.image.get_size()
        image_area = image_width * image_height
        sample_gap = max(3, math.ceil(math.sqrt(image_area / MAX_PARTICLES)))
        base_radius = max(1, sample_gap // 3)

        centre = pygame.Vector2(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2)
        outer_distance = math.hypot(*WINDOW_SIZE) * 0.63
        particles = []

        for image_y in range(0, image_height, sample_gap):
            for image_x in range(0, image_width, sample_gap):
                pixel = self.image.get_at((image_x, image_y))

                # Skip transparent and nearly-black background pixels.
                if pixel.a < 30 or max(pixel.r, pixel.g, pixel.b) < 32:
                    continue

                angle = random.uniform(0.0, math.tau)
                distance = outer_distance + random.uniform(-120.0, 150.0)

                start = centre + pygame.Vector2(
                    math.cos(angle) * distance,
                    math.sin(angle) * distance,
                )

                target = pygame.Vector2(
                    self.image_rect.left + image_x,
                    self.image_rect.top + image_y,
                )

                particles.append(
                    Particle(
                        start=start,
                        target=target,
                        colour=(pixel.r, pixel.g, pixel.b),
                        radius=random.choice((base_radius, base_radius, base_radius + 1)),
                        delay=random.uniform(0.0, 2.2),
                        travel_time=random.uniform(2.4, 4.2),
                        phase=random.uniform(0.0, math.tau),
                    )
                )

        random.shuffle(particles)
        return particles

    def restart(self):
        self.particles = self._create_particles()
        self.elapsed = 0.0

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_r:
                    self.restart()

        return True

    def _draw_background(self):
        self.screen.fill(BACKGROUND)

        pulse = (math.sin(self.elapsed * 1.8) + 1.0) / 2.0
        for x, y, radius, brightness in self.stars:
            value = min(255, int(brightness + pulse * 40))
            pygame.draw.circle(self.screen, (value, value, value), (x, y), radius)

    def _draw_particles(self):
        self.glow_layer.fill((0, 0, 0, 0))
        visible_particles = []

        for particle in self.particles:
            result = particle.position_at(self.elapsed)
            if result is None:
                continue

            position, progress = result
            point = (round(position.x), round(position.y))
            visible_particles.append((particle, point))

            if progress > 0.82:
                glow_alpha = int(22 + 38 * progress)
                pygame.draw.circle(
                    self.glow_layer,
                    (*particle.colour, glow_alpha),
                    point,
                    particle.radius * 4,
                )

        self.screen.blit(self.glow_layer, (0, 0))

        for particle, point in visible_particles:
            pygame.draw.circle(
                self.screen,
                particle.colour,
                point,
                particle.radius,
            )

    def _draw_final_image(self):
        fade_progress = (self.elapsed - REVEAL_AT) / REVEAL_SECONDS
        if fade_progress <= 0:
            return

        final_image = self.image.copy()
        final_image.set_alpha(round(255 * smoothstep(fade_progress)))
        self.screen.blit(final_image, self.image_rect)

    def run(self):
        running = True

        while running:
            seconds = self.clock.tick(FPS) / 1000.0
            self.elapsed += seconds
            running = self._handle_events()

            self._draw_background()
            self._draw_particles()
            self._draw_final_image()

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    KrishnaParticleApp().run()

from solvers.module_solver import ModuleSolver
from overlay.recorder import Recorder
from overlay.overlay import Overlay
import time

FPS = 30
import threading


def main():
    recorder = Recorder()
    overlay = Overlay()
    threading.Thread(target=Overlay)
    module_solver = ModuleSolver()
    while True:
        start_time = time.perf_counter()
        action = module_solver.solve(recorder.get_frame())
        overlay.display_action(action)
        elapsed = time.perf_counter() - start_time
        time_to_sleep = 1 / FPS - elapsed
        time.sleep(max(time_to_sleep, 0))


if __name__ == "__main__":
    main()

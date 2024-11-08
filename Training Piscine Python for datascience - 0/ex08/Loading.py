import time
import shutil


def format_time(seconds):
    """
    Modify the format of time given in seconds as MM:SS.

    Args :
        seconds (float): Time to format.

    Returns :
        string: formatted to MM:SS.
    """
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range) -> None:
    """
    Simulate a loading bar while iterating throught a range.

    Args :
        lst (range): The range to iterate throught.
    """
    # Get the total lenght of lst to calculate the progression
    total = len(lst)
    # Save the starting time of iteration to calculate the time flow
    start_time = time.time()

    # Get the width of the terminal minus 30 char to print informations
    terminal_width = shutil.get_terminal_size().columns - 30
    # Adjust progression bar width to fit in terminal
    progress_bar_width = terminal_width - 10

    for i, item in enumerate(lst, start=1):
        # Calcul the actual progress in nb of char for the bar
        progress = int(i / total * progress_bar_width)
        # Calcul the elapsed time from begining
        elapsed_time = time.time() - start_time
        # Calcul the iteration speed per seconds
        speed = i / elapsed_time
        # Calcul the time left depending on actual speed
        eta = (total - i) / speed

        # Formate the elasped time in good format
        elapsed_formatted = format_time(elapsed_time)
        # Formate the time left in good format
        eta_formatted = format_time(eta)

        # Create the virtual progression bar filled with █
        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        # Calculate the percentage of progression
        progress_percentage = progress * 100 // progress_bar_width
        # Create the display of percentage of progress bar and actual
        # position depending on total
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        # Create a string contening the elapsed time and speed (iteration/sec)
        time_info = f"[{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"

        # Print progression with \r to actualize instead of creating new line
        print(f"\r{progress_info} {time_info}", end="", flush=True)
        # Generator which keeps iteraring on lst and displaying progress bar
        yield item


def main():
    for _ in ft_tqdm(range(0, 333)):
        pass


if __name__ == "__main__":
    main()

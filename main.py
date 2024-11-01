from moviepy.editor import VideoFileClip


def mp4_to_gif(mp4_path, gif_path, start_time=0, end_time=None, fps=10):
    """
    Converts an MP4 video to a GIF.

    Parameters:
    - mp4_path: str, path to the .mp4 file
    - gif_path: str, path to save the .gif file
    - start_time: int, start time in seconds (default: 0)
    - end_time: int, end time in seconds (default: None, till the end of video)
    - fps: int, frames per second for the GIF (default: 10)
    """
    clip = VideoFileClip(mp4_path)

    if end_time:
        clip = clip.subclip(start_time, end_time)

    clip.write_gif(gif_path, fps=fps)
    print(f"GIF saved to {gif_path}")

    """
    - insert the file path of your mp4 file and name the output .gif file and if you want the output path. 
    - By default it will create it inside your repository directory
    - Choose your custom parameters 
    """

mp4_to_gif("input.mp4", "output.gif", start_time=15, end_time=28, fps=15)

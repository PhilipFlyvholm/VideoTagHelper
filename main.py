#!/usr/bin/env python
import ffmpeg
import os.path


def main():
    video_input = load_video()
    print("Write out folder path (enter for current folder)")
    output_folder_path = input()

    output_folder_path = handle_file_drag(output_folder_path)
    if output_folder_path != "":
        output_folder_path += "/"
    else:
        output_folder_path = "./"
    formats = get_file_formats()

    #Output as .mp4, .ogg, .webm using ffmpeg
    isExist = os.path.exists(output_folder_path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(output_folder_path)
    for format in formats:
        video_input.output(output_folder_path + "output." + format).run()
    video_input.output(output_folder_path + "output.jpeg", vframes=1).overwrite_output().run(capture_stdout=True, capture_stderr=True)

def get_file_formats():
    print("Write file formats needed as a comma seperated list (mp4,webm)")
    input_formats = input()
    if len(input_formats) == 0:
        print("No input given. Please try again")
        return get_file_formats()
    return input_formats.split(",")

def handle_file_drag(str):
    if str.startswith("'") and str.endswith("'"):
        return str[1:-1]
    return str
    

def load_video():
    print("Write input file path:")
    input_path = input()
    input_path = handle_file_drag(input_path)
    if os.path.isfile(input_path):
        try:
            return ffmpeg.input(input_path)
        except:
            print(input_path + " is not a valid file type")
            return load_video()
    else:
        print(input_path + " is not a valid file path")
        return load_video()

if __name__ == '__main__':
    main()

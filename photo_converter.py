from PIL import Image
import moviepy.editor as mp
import os


def convert_image(input_path, output_format, output_directory):
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Create the output path
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            output_path = os.path.join(output_directory, f"{base_name}.{output_format}")
            # Save the image in the new format
            img.save(output_path)
            print(f"Image converted and saved as: {output_path}")
    except Exception as e:
        print(f"Error converting image: {e}")

def convert_video(input_path, output_format, output_directory):
    try:
        # Load the video
        clip = mp.VideoFileClip(input_path)
        # Create the output path
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = os.path.join(output_directory, f"{base_name}.{output_format}")
        # Save the video in the new format
        clip.write_videofile(output_path)
        print(f"Video converted and saved as: {output_path}")
    except Exception as e:
        print(f"Error converting video: {e}")

def main():
    input_path = input("Enter the file path (image or video): ").strip()
    output_format = input("Enter the desired format (jpg, png, webm, mp4, etc.): ").strip()
    output_directory = input("Enter the output directory: ").strip()

    if not os.path.exists(input_path):
        print("The specified file does not exist.")
        return

    if not os.path.exists(output_directory):
        print("The specified output directory does not exist.")
        return

    # Detect the file type
    ext = os.path.splitext(input_path)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
        convert_image(input_path, output_format, output_directory)
    elif ext in ['.mp4', '.webm', '.avi', '.mov', '.mkv']:
        convert_video(input_path, output_format, output_directory)
    else:
        print("Unsupported format.")

os.system('cls||clear')

print("""
           d8b                                                                                                            
           ?88                 d8P                                                                   d8P                  
            88b             d888888P                                                              d888888P                
?88,.d88b,  888888b  d8888b   ?88'   d8888b      d8888b d8888b   88bd88b ?88   d8P d8888b  88bd88b  ?88'   d8888b  88bd88b
`?88'  ?88  88P `?8bd8P' ?88  88P   d8P' ?88    d8P' `Pd8P' ?88  88P' ?8bd88  d8P'd8b_,dP  88P'  `  88P   d8b_,dP  88P'  `
  88b  d8P d88   88P88b  d88  88b   88b  d88    88b    88b  d88 d88   88P?8b ,88' 88b     d88       88b   88b     d88     
  888888P'd88'   88b`?8888P'  `?8b  `?8888P'    `?888P'`?8888P'd88'   88b`?888P'  `?888P'd88'       `?8b  `?888P'd88'     
  88P'                                                                                                                    
 d88                                                                                                                      
 ?8P                                                                                                                      
    """)

if __name__ == "__main__":
    main()
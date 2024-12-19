import os
import subprocess
import glob
import multiprocessing

input_folder = r"map1"
output_folder = r"map2"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def convert_to_gif(file_path):
    # Bepaal de naam van het output bestand
    base_name = os.path.basename(file_path)
    output_file = os.path.join(output_folder, f"{os.path.splitext(base_name)[0]}.gif")
    
    # Volledige pad naar ffmpeg.exe
    ffmpeg_path = r"locatie/download"  # Locatie waar je de ffmpeg hebt gedownload
    
    # Controleer of het GIF-bestand al bestaat
    if os.path.exists(output_file):
        print(f"{output_file} bestaat al. Sla over.")
        return  # Sla de conversie over als het bestand al bestaat

    # FFmpeg command
    command = [
        ffmpeg_path, '-i', file_path, 
        '-vf', 'fps=10,scale=320:-1:flags=lanczos', 
        '-c:v', 'gif', 
        output_file
    ]
    
    # Voer het commando uit
    subprocess.run(command)
    print(f"Converted {file_path} to {output_file}")

def main():
    # Zoek naar MP4 bestanden in de input folder
    mp4_files = glob.glob(os.path.join(input_folder, '*.mp4'))
    
    # Gebruik multiprocessing om bestanden in bulk te converteren
    with multiprocessing.Pool() as pool:
        pool.map(convert_to_gif, mp4_files)

if __name__ == '__main__':
    main()

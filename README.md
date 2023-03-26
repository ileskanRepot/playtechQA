# How use

First you need to install Python39 and selenium (If you are using nixos you can just type `nix-shell`). Then you can just type `python app.py`

# How I solved this

- Setup chromedriver to my `nix-shell`

- I opened `https://www.playtech.ee` at normal web browser and checked what happens.

- Saw cookie popup so first thing was to click that away.

- Check what is that buttons className and used that

- Then search for the actual `internship` tab

  - There was two internship text nodes so I had to think other way to identify my link

- Click the link

- Then check if there is element with text `Development QA Engineer (Intern)`

- Write result and timestamp to file `logs.txt`

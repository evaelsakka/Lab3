
# ABOUT FILTERED IMAGE

This simple python script takes a user-specified image path, applies a chosen filter to it, and saves the filtered image in the same directory of the original image. 

Since it doesn't have a GUI yet, you need to use the command-line shell on your computer to run it.

## HOW TO ?

Download the `FilteredImage.py` file from the repo and make sure that Python 3 is already installed on your computer. 

Since this program uses the `Pillow` module (A fork of the Python Imaging Library `PIL` that provides support for opening, manipulating, and saving many different image file formats), you also need to have this module installed. 

To do so, open your command-line shell and run the following command:

```bash
pip install Pillow
```

Now you should be all set to run the program without any issues. 

In your command-line shell, switch to the directory where you downloaded the `FilteredImage.py` file and run the following command: 

```bash
python3 FilteredImage.py
```

A prompt will ask you to enter the path of the image file you want to apply a filter to.

Make sure to enter a valid image path, and hit `enter`/`return` on your keyboard.

Another prompt should ask you to choose one of four filter types; `grayscale`, `error_diffusion`, `sepia`, and `negative`.

Make sure to enter a valid filter type and also hit the `enter`/`return` key on your keyboard.

A new image with the applied filter should be processed and saved in the same directory of the original image. 

A success message for the execution should print out on your command-line shell, and the program will then terminate.

## ISSUES ?

If you're running into any issues, let us know about them on `https://github.com/evaelsakka/Lab3/issues`.

import sys
from PIL import Image, ImageOps


def main():
    original_picture, new_picture = get_picture()
    overlay(original_picture, new_picture)




def get_picture():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command line arguments")
        return sys.argv[1], sys.argv[2]
    except IndexError:
        sys.exit("Out of range")



def overlay(original_picture, new_picture):
    overlay_image = Image.open("shirt.png")
    try:
        check1, check2 = original_picture.split(".")
        check3, check4 = new_picture.split(".")
        if check2.lower() and check4.lower() not in ["jpg", "jpeg", "png"]:
            sys.exit("Invalid picture format")
        elif check2.lower() != check4.lower():
            sys.exit("Error. Different image types")
        else:
            with Image.open(original_picture, "r") as picture:
                resized_picture = ImageOps.fit(picture, (600, 600))
                resized_picture.paste(overlay_image, (0, 0), overlay_image)
                resized_picture.save(new_picture)
                resized_picture.show()
    except FileNotFoundError:
        sys.exit(f"File with name \"{original_picture}\" not found")
    except Exception as e:
        print(e)











if __name__ =="__main__":
    main()
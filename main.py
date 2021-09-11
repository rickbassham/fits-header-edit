import argparse
import glob
from typing import Any

from astropy.io import fits


def edit_fits_headers(
    path: str, header: str, value: Any, recursive: bool = False
) -> None:
    for file_path in glob.iglob(path, recursive=recursive):
        print(f"{file_path} : {header}={value}")

        fits.setval(
            file_path,
            header,
            value=value,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set FITS file headers.")
    parser.add_argument("-p", "--path", help="path to the FITS file(s)", required=True)
    parser.add_argument("--header", help="header name to set", required=True)
    parser.add_argument("--value", help="value to set", required=True)
    parser.add_argument(
        "-r",
        "--recursive",
        help="recursive search",
        default=False,
        action="store_true",
    )
    args = parser.parse_args()

    edit_fits_headers(args.path, args.header, args.value, args.recursive)

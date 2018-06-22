import CanvasAPI
import logging

def get_course(course_id):
    course = CanvasAPI.courses.get(course_id)
    CanvasAPI.util.printer.print_odict(course)

if __name__ == "__main__":
    for row in CanvasAPI.util.file.get_data(["course_id"]):
        try:
            get_course(row[0])
        except Exception as e:
            logging.warning("Error with '{}': {}".format(", ".join(row), e))
            continue
    input("Press enter to close...")

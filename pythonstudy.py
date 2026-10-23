# from pathlib import Path

file_path = Path("student.txt")

# file_path.write_text("Name:Tamil\nCourse:python",
#                      encoding="utf-8")

# print("file writen successfully")

# content=file_path.read_text(encoding="utf-8")

# print(content)

# with file_path.open("a",encoding="utf-8") as file:
#     file.write("\nMarks:85")

# print(file_path.read_text(encoding="utf-8"))




# fast api
from pathlib import Path
from fastapi import FastAPI

app = FastAPI()

file_path = Path("student.txt")

@app.get("/")
def home():
    return {
        "Name": "Tamil",
        "Course": "Python",
        "Marks": 85
    }
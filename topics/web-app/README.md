# Baseline Skills for Flask

## First, ask yourself if you know how to
- [ ] Create basic HTML elements (e.g. tables, ordered/unordered lists, hyperlinks, images)
- [ ] Style page using CSS (inline, internal, external CSS)
- [ ] Set up project subfolders and files, e.g. app.py, index.html for Flask and display a HTML page
- [ ] Define routes, setting `methods=["GET", "POST"]` where necessary
- [ ] Use `render_template()` to pass Python variables to Jinja2 templates
- [ ] Use `{{ ... }}`, `{% for ... %}`, `{% if ... %}` for Jinja2
- [ ] Use `url_for()` and `redirect()`
- [ ] Create a form and submitting data using `GET` or `POST`
- [ ] Access query parameters in a URL using `request.args.get()`. Access form data via `POST` request using `request.form.get()`
- [ ] Read and write data for flat files (text / CSV) in web app
- [ ] Perform CRUD operations for SQLite3 database in web app
- [ ] Handle file uploads: (a) check file extensions, (b) use `secure_filename(filename)` from `werkzeug.utils` to sanitise filenames, (c) using `os.path.join(directory, filename)`, (d) using `file.save(filepath)`, (e) in HTML, write `<form method="POST" action="/upload" enctype="multipart/form-data">`

## 1. Basic Flask Setup  -- JC1 Standard: within 5 min
- Reminder: **NO RIGHT-CLICKING IS ALLOWED**.
- Create `Task4_4` main folder on Desktop.
- Create `index.html`, linking to external CSS `style.css`.
- Display the following:
  Black background, white text, Arial.
  Centralised table with 2 rows and 3 columns.
  Cells in second row has height and width of 100px.

![image](https://github.com/user-attachments/assets/112e4c62-4a59-4b03-9c3d-8fdf0de4969c)

---

## 2. Flask with Factorial and Fibonacci Numbers -- JC1 Standard: within 8 min
- Write two functions `factorial(n)` and `fib(n)` that run iteratively using for loop
- Display the results for n = 0 to 30 (inclusive) in a table, ensuring border and centralised text.
- No need for external CSS.
  
![image](https://github.com/user-attachments/assets/92e1021a-e0e4-4498-8dc5-855c3f238fc1)

---

## 3. Flask with Fibonacci Numbers and Factors
- Write a recursive version of `fib(n)`. Note that this will be **highly inefficient**, with **exponential time complexity**!
- Write a function `factors(num)` that returns a **string** of all positive factors of `num`, e.g. `factors(6)` returns the string `1, 2, 3, 6`.
- Display a table showing results for n = 0 to 20, with columns: n, fib(n), positive factors of fib(n).
- No need for external CSS.

![image](https://github.com/user-attachments/assets/ad07e4f4-4335-4d83-a582-61a94888fac2)




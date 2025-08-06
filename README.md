
# Unit Converter

A simple web application built with Django to convert between selected units of measurement including length, weight, and temperature.


https://roadmap.sh/projects/unit-converter



## Supported Units

- **Length:** millimeter (mm), centimeter (cm), meter (m), kilometer (km), inch (in)  
- **Weight:** milligram (mg), gram (g), kilogram (kg), ton (t)  
- **Temperature:** Celsius (°C), Fahrenheit (°F), Kelvin (K)

---

## How It Works

- Separate pages handle conversion for length, weight, and temperature.  
- Each page contains a form where users enter the numeric value and select source and target units from the supported list.  
- Upon submission, Django processes the input, performs the conversion using standard formulas, and returns the result on the same page.  
- No database is used; all conversions are done in the backend views.

---

## Technologies Used

- Backend: Django (Python)  
- Frontend: HTML, CSS, js

---


## Notes

- Input validation is performed to ensure numeric values.  
- Only the units listed above are supported currently.  
- The project can be extended to add more units and features.

---

Thank you for exploring this project!

# QColor
Awesome Sublime Color Highlighter, Converter and Picker 


## Installation
1. `pip3 install pywebview`
2. Restart Sublime


## Settings
`phantom_shape` - Shape of the color phantom displayed, "square" or "circle".

`hsl_float` - Sets HSL color precision to 3 decimal places. Default is 0 decimal places.

`hex_upper_case` - Display hex values in upper case.

`hover_preview` - Enable a color preview when hovering over a color.

`named_colors` - Enable phantoms for named colors such as "red", "blue".
[Available names here.](https://www.december.com/html/spec/colorsvg.html)


## Menu Options
`QColor: Picker` - Open the pywebview color picker.

`QColor: Show` - Enable QColor plugin.

`QColor: Toggle` - Enable and disable QColor plugin

`QColor: Settings` - Edit the QColor settings files.

`QColor: Key Bindings` - Edit the QColor key bindings.


## Screenshots
|Picker|Converter|
|:----:|:-------:|
|![Screenshot from 2021-09-04 15-53-27](https://user-images.githubusercontent.com/2568375/132105273-a454bfa7-0f11-4e6b-b141-20654e36fe8c.png) | ![image](https://user-images.githubusercontent.com/2568375/109458175-0fb34c80-7a3b-11eb-8185-a92a24f98f38.png)


## Possible problems
If picker dont works, maybe you having some problem with pywebview. You can try
run the following python code to check if webview is working properly.
```python
import webview
webview.create_window('Hello world', 'https://pywebview.flowrl.com/hello')
webview.start()
```

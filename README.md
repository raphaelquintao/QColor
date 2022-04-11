# QColor
Awesome Sublime Color Highlighter, Converter and Picker 


## Installation
1. `pip3 install pywebview`
2. Restart Sublime


## Settings
**phantom_shape**  - Shape of the color phantom displayed, "square" or "circle".<br/>
**hsl_precision**  - Number of decimal places in HSL precision.<br/>
**hex_upper_case** - Display hex values in upper case.<br/>
**hover_preview**  - Enable a color preview when hovering over a color.<br/>
**named_colors**   - Enable phantoms for [named colors](https://www.december.com/html/spec/colorsvg.html)
                     such as "red", "blue".<br/>

### Menu Options
**QColor: Picker** - Open the pywebview color picker.<br/>
**QColor: Show Colors** - Show color phantoms.<br/>
**QColor: Hide Colors** - Hide color phantoms.<br/>
**QColor: Toggle Colors** - Toggle color phantoms.<br/>
**QColor: Settings** - Edit the QColor settings files.<br/>
**QColor: Key Bindings** - Edit the QColor key bindings.<br/>

### Key Bindings
`ctrl+shift+c` - Open the color picker.<br/>
`alt+shift+c` - Open the color convertor.<br/>
`alt+ctrl+c` - Toggle color phantoms.<br/>


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

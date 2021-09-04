# QColor
Awesome Sublime Color Highlighter, Converter and Picker 

## Installation
1. `pip3 install pywebview`
2. Restart Sublime

### Possible problems
  
If picker dont works, maybe you having some problem with pywebview. You can try run the following python code to check if webview is working properly.

```python

import webview
webview.create_window('Hello world', 'https://pywebview.flowrl.com/hello')
webview.start()

```

## Settings
```
{
  "__debug": false,
  "_enabled": true,
  "q_color": // is used internally, it recommended not change. 
  {
    "active": false 
  },
  "circular_phantom": true,
  "hsl_float": false,
  "hex_upper_case": true,
  "hover_preview": false,
  "auto_close_popups": true,
  "named_colors": false
}
```

## Screenshots
|Picker|Converter|
|:---:|:---:|
|![Screenshot from 2021-09-04 15-53-27](https://user-images.githubusercontent.com/2568375/132105273-a454bfa7-0f11-4e6b-b141-20654e36fe8c.png) | ![image](https://user-images.githubusercontent.com/2568375/109458175-0fb34c80-7a3b-11eb-8185-a92a24f98f38.png)


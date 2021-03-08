# QColor
Awesome Sublime Color Highlighter, Converter and Picker 

## Installation
1. `pip3 install pywebview`
2. Restart Sublime

### Possible problems
  
If picker dont works, maybe you having some problem with pywebview. You can try run the following python code to check if webview is working preperly.

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
  "q_color":
  {
    "active": false
  },
  "circular_phantom": true,
  "hsl_float": true,
  "hex_upper_case": true,
  "hover_preview": true,
  "auto_close_popups": true,
  "named_colors": false
}
```

## Screenshots
![image](https://user-images.githubusercontent.com/2568375/109458175-0fb34c80-7a3b-11eb-8185-a92a24f98f38.png)
![image](https://user-images.githubusercontent.com/2568375/109461386-d251bd80-7a40-11eb-99c1-4da7d375433b.png)
![image](https://user-images.githubusercontent.com/2568375/109461430-e4336080-7a40-11eb-8bb8-f64aed41e0b6.png)


function main() {
    var close = document.getElementById('close');
    close.onclick = () => {
        closeWindow(false)
        // window.close()
    }
    var save = document.getElementById('save');
    save.onclick = () => {
        closeWindow(true)
        // window.close()
    }

    var value = document.getElementById('value');
    var alpha = document.getElementById('alpha');


    // var input = document.getElementById('colorInput1');
    // input.value=_color;

    function catchException() {
        pywebview.api.error().catch(showResponse)
    }

    window.addEventListener('pywebviewready', () => {
        // var container = document.getElementById('response-container')
        // container.innerHTML = '<i>pywebview</i> is ready'
        // container.style.display = 'block'
        getTitle();

    })
    function showResponse(response) {
        var container = document.getElementById('response-container')

        container.innerText = response.message
    }

    setColor = (response) => {
        var container = document.getElementById('colorInput1')
        container.value = response.message
        // container.trigger("onInput");

        value.value = response.message

        var myPicker = new JSColor('#colorInput1');
        // myPicker.option('position', 'right');
        myPicker.option({
            'format': 'any',
            'width': 250,
            'height': 250,
            'previewSize': 32,
            'hideOnLeave': false,
            'closeButton': false,
            'backgroundColor': "#333",
            'borderColor': '#000',
            'controlBorderColor': '#000',
            'controlBorderColor': '#000',
            'pointerBorderColor': 'rgba(0,0,0,0.9)',
            'pointerColor': 'rgba(255,180,200,0.9)',
            'pointerBorderWidth': 1,
            'pointerThickness': 2,
            'borderWidth': 0,
            'borderRadius': 0,
            'shadow': false,
            'container': document.getElementById('container'),
            'previewElement': document.getElementById('preview'),
            'alphaElement': document.getElementById('alpha'),
            // 'valueElement': document.getElementById('value'),
        });
        myPicker.onChange = (v) => {
            // alert(myPicker);
            greet();
        }
        myPicker.show();
        value.onkeyup = (e) => {
            if (e.key == 'ArrowLeft') return             
            if (e.key == 'ArrowRight') return
            if (e.key == 'ArrowUp') return
            if (e.key == 'ArrowDown') return
            if (e.key == 'Shift') return
            if (e.key == 'Control') return
            if (e.key == 'Alt') return

            myPicker.fromString(e.target.value);
            greet();
            // e.target.value=e.key;
            // alert(e.target.value);

        }

        alpha.onchange = (e) => {
            // closeWindow()
            // window.close()
            myPicker.channel('A', e.target.value);
            greet();
            // alert(e.target.value);

        }
    }

  

    function initialize() {
        pywebview.api.init().then(showResponse)
    }

    function getRandomNumber() {
        pywebview.api.getRandomNumber().then(showResponse)
    }
    function greet(show = true) {
        var name_input = document.getElementById('colorInput1').value;
        pywebview.api.showColor(name_input).then(showResponse)

        if(value.value.replace(/\s/g, '') != name_input.replace(/\s/g, ''))
            value.value = name_input;
    }

    function getTitle() {
        pywebview.api.getTitle("asd").then(setColor)
    }

    function closeWindow(to_print) {
        // alert("asdasd");
        pywebview.api.closeWindow(to_print)
    }


    // jscolor.presets.default = {
    //     format: 'any',
    //     width: 101,
    //     backgroundColor: '#333'
    // }

    
    // jscolor.trigger("change input");
    
    // myPicker.show();
    


}
// initialize();

// main()
// window.addEventListener("DOMContentLoaded", main);
window.addEventListener("load", main);
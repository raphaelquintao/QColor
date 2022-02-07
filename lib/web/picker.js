function is_webview() {
    return (typeof window.pywebview !== 'undefined');
}

function initialize() {
    if (is_webview()) pywebview.api.init().then(showResponse);
}

function init() {
    if (is_webview()) {
        pywebview.api.start().then(r => { set_color(r.data) });;
    } else set_color('#ff0000');
}


function send_color(color, show = true) {
    if (is_webview()) pywebview.api.showColor(color).then(r => { show_response(r.data) });
    else show_response(color);
    // if (webview()) pywebview.api.showColor(color);
    // if (value.value.replace(/\s/g, '') != name_input.replace(/\s/g, ''))
    // value.value = name_input;
}


function show_response(response) {
    let container = document.getElementById('response');
    container.innerText = JSON.stringify(response);
}


function closeWindow(to_print) {
    if (is_webview()) pywebview.api.closeWindow(to_print);
    else console.log(to_print);
}

function set_color(color) {
    var input_color = document.getElementById('value');
    var input_alpha = document.getElementById('alpha');

    input_color.value = color;

    let myPicker = new JSColor(input_color, {
        format: 'rgba',
        previewSize: 0,
        previewPadding: 0,
        width: 250,
        height: 250,
        hideOnLeave: false,
        closeButton: false,
        backgroundColor: "var(--page-bg-color)",
        borderColor: 'red',
        controlBorderColor: 'var(--border-color)',
        pointerBorderColor: 'var(--border-color)',
        pointerColor: 'var(--text-color)',
        sliderSize: 16,
        crossSize: 8,
        pointerBorderWidth: 1,
        pointerThickness: 2,
        borderWidth: 0,
        borderRadius: 0,
        shadow: false,
        container: document.getElementById('container'),
        previewElement: document.getElementById('preview'),
        alphaElement: input_alpha,
        valueElement: input_color,
    });
    myPicker.onChange = (v) => {
        send_color(myPicker.toRGBAString());
    }
    input_alpha.onchange = (e) => {
        myPicker.channel('A', e.target.value);
        send_color(myPicker.toRGBAString());
    }

    myPicker.show();



};

function main() {
    let btn_save = document.getElementById('save');
    let btn_close = document.getElementById('close');
    let response = document.getElementById('response');

    if(!is_webview()){
        response.style.display = 'none';
    }

    btn_save.onclick = () => {
        closeWindow(true);
    }

    btn_close.onclick = () => {
        closeWindow(false);
    }



    function catchException() {
        pywebview.api.error().catch(showResponse)
    }


    window.addEventListener('pywebviewready', () => {
        init();
    });

    setTimeout(() => {
        if (!is_webview()) init();
    }, 100);
}

window.addEventListener("load", main);
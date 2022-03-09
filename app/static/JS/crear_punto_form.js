const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('input');

const campos = {
    nombre: false,
    longitud: false,
    latitud: false,
    email: false,
    telefono: false,
    direccion: false
}

const patterns = {
    nombre: /^[a-zA-ZÀ-ÿ\s0-9]{4,150}$/,
    longitud: /^[+-]?((([1-9]?[0-9]|1[0-7][0-9])(\.[0-9]{1,6})?)|180(\.0{1,6})?)$/,
    latitud: /^[+-]?(([1-8]?[0-9])(\.[0-9]{1,6})?|90(\.0{1,6})?)$/,
    email: /^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$/,
    telefono: /^\d{7,14}$/,
    direccion: /.{7,150}/
};

inputs.forEach((input) => {
    input.addEventListener('keyup', (e) => {
        validate(e.target, patterns[e.target.attributes.id.value], e.target.attributes.id.value);
    });
    input.addEventListener('blur', (e) => {
        validate(e.target, patterns[e.target.attributes.id.value], e.target.attributes.id.value);
    });
});

function validate(field, regex, campo) {
    if (regex.test(field.value)) {
        field.className = 'form-control input-forms-valid';
        document.getElementById(`mensaje-ayuda-${campo}`).className = 'mensaje-ayuda-form-desactivado';
        campos[field.id] = true;
    } else {
        field.className = 'form-control input-forms-invalid';
        document.getElementById(`mensaje-ayuda-${campo}`).className = 'mensaje-ayuda-form-activado';
        campos[field.id] = false;
    }
}

formulario.addEventListener('submit', (e) => {

    const publicado = document.getElementById('publicado');
    const despublicado = document.getElementById('despublicado');
    if (!campos.nombre || !campos.longitud || !campos.latitud || !campos.email || !campos.telefono || !campos.direccion || (!publicado.checked && !despublicado.checked)) {
        e.preventDefault();
        document.getElementById('formulario_mensaje').classList.remove('formulario_mensaje_desactivado');
        document.getElementById('formulario_mensaje').classList.add('alert');
        document.getElementById('formulario_mensaje').classList.add('alert-danger');
        document.getElementById('formulario_mensaje').classList.add('mb-3');
        setTimeout(() => {
            document.getElementById('formulario_mensaje').classList.remove('alert');
            document.getElementById('formulario_mensaje').classList.remove('alert-danger');
            document.getElementById('formulario_mensaje').classList.remove('mb-3');
            document.getElementById('formulario_mensaje').classList.add('formulario_mensaje_desactivado');
        }, 5000);
    } else {
        formulario.submit();
    }
});
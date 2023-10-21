console.log('fucinou')

function validateForm() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;


    if (username === 'lizael17' && password === 'l12345678') {
        alert('Login bem-sucedido!');
        return true;
    } else {
        alert('Nome de usuário ou senha incorretos. Tente novamente.');
        return false;
    }
}
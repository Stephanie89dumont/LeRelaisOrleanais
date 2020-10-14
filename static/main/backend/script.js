function myOpen(id) {
    var elem = document.getElementById(id);
    if (id == "contact") {
        var elem2 = document.getElementById("bandeau1");
    } else {
        var elem2 = document.getElementById("bandeau2")
    }
    var pos = 0;
    var pos2 = -25;
    var id = setInterval(frame, 8);

    function frame() {
        if (pos == 25) {
            clearInterval(id);
        } else {
            pos++;
            elem.style.right = pos + "vh";
        }
        if (pos2 == 0) {
            clearInterval(id);
        } else {
            pos2++;
            elem2.style.right = pos2 + "vh";
        }
    }
}

function myClose(id) {
    var elem = document.getElementById(id);
    if (id == "bandeau1") {
        var elem2 = document.getElementById("contact");
    } else {
        var elem2 = document.getElementById("profil")
    }
    var pos = 25;
    var pos2 = 0;
    var id = setInterval(frame, 8);

    function frame() {
        if (pos == 0) {
            clearInterval(id);
        } else {
            pos--;
            elem2.style.right = pos + "vh";
        }
        if (pos2 == -25) {
            clearInterval(id);
        } else {
            pos2--;
            elem.style.right = pos2 + "vh";
        }
    }
}

function reveal(id) {
    if (document.getElementById(id).className == "far fa-eye-slash") {
        var x = document.getElementsByClassName("password");
        document.getElementById(id).className = "far fa-eye";
        var i;
        for (i = 0; i < x.length; i++) {
            x[i].type = "text";
        }
    } else {
        var x = document.getElementsByClassName("password");
        document.getElementById(id).className = "far fa-eye-slash";
        var i;
        for (i = 0; i < x.length; i++) {
            x[i].type = "password";
        }
    }
}

let d1 = document.getElementById("d1");
let p1 = document.getElementById("p1");

d1.addEventListener("mouseout", () => {
        p1.style.display = "none";
    }

);
d1.addEventListener("mouseover", () => {
        p1.style.display = "block";

    }

);
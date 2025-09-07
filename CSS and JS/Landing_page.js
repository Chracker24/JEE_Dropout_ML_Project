document.addEventListener("DOMContentLoaded", () => {
    const subline = document.getElementById("subline_jeet");
    const text = " An Early warning tool for students, before their careers even start !";
    let index  = 0;

    function type(){
        if (index < text.length) {
            subline.innerHTML += text.charAt(index);
            index++;
            setTimeout(type, 80);
        }
             
    }

    type();

    const button = document.querySelector(".JEET_button");
    button.addEventListener("click", () => {
        console.log("JEET button clicked and getting redirected ");
        window.open("https://jeetprep.streamlit.app/", "_blank")
    });

    const steps = document.querySelectorAll(".How_step");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("active"); // animate in
        }
        });
    }, { threshold: 0.3 }); // trigger when 30% visible

    steps.forEach(step => observer.observe(step));
})


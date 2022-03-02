const form=document.querySelector("form");
console.log(form);

function submitForm(event){
    event.preventDefault();
    const data=new FormData(form);
    console.log(data);

    const params=new URLSearchParams();
    for(pair of data){
        params.append(pair[0],pair[1].toString());
    }
    console.log(params);

    fetch('/', {method:'POST', body:params})
    .then(response=>response.json())
    .then((data)=>{
        console.log(data)
        
        if(data.status==='done'){
            form.reset()
            document.querySelector(".message").innerText=data.message;
        }
        else if(data.status==='invalid'){
            for(const error in data.errors){
                console.log(error);
                console.log(data.errors[error][0].message);
    
                const errorField=document.querySelector(`#id_${error}`);
                errorField.focus();
    
                errorField.parentElement.classList.add('error-field')
    
                const helpSpan=document.querySelector(`#id_${error} + span.helptext`);
                console.log(helpSpan);
    
                helpSpan.innerText=data.errors[error][0].message;
            }
        }
    })
    .catch(error=>console.log(error))


}

form.addEventListener("submit", submitForm);
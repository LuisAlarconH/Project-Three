$(document).ready(function() {
    $('#example').DataTable({     
      "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
        "iDisplayLength": 3
       } 
    );
} );

function verify() {
  var nbr;
  nbr = Number(document.getElementById("age").value);
  if (nbr < 18)
  {
    alert("You are under the age of 18, which means you will be entered in the raffle however you would need to be supervised by an adult")

  }
  else
  {
    alert("You are an adult, you have now been entered in the raffle")
  }
}

const btnDelete= document.querySelectorAll('.btn-delete');
if(btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      if(!confirm('Are you sure you want to remove participant?')){
        e.preventDefault();
      }
    });
  })
}
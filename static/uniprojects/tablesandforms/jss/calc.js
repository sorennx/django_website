function sumFields(){
    let l1 = document.getElementById('l1').value;
    let l2 = document.getElementById('l2').value;
    let sum = parseInt(l1) + parseInt(l2);

    let sumField = document.getElementById('suma');
    sumField.value = sum;
}

function calcInstallment(){
    let k = parseInt(document.getElementById('kwota').value);
    let pr = parseInt(document.getElementById('procent').value)/100;
    let n = parseInt(document.getElementById('ilerat').value);

    let pr_mc = pr/12;
    let rata = (k*pr_mc)/(1-(1/(1+pr_mc)**n));

    document.getElementById('ratamiesieczna').value = rata.toFixed(2);
    document.getElementById('kwotazodsetkami').value = (rata*n).toFixed(2);

    // let rm = document.getElementById('ratamiesieczna');
    // let total = document.getElementById('kwotazodsetkami');
    // rm.value = rata;
    // total.value = rata*10;
}
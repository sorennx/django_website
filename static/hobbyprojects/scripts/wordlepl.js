function test()
{
    let res = document.getElementById('row0_res');
    let row1 = document.getElementsByClassName('tile_input_r1');
    for(let i=0; i<row1.length; i++)
    {
        res.value+=row1[i].value.toUpperCase();
    }
    console.log(":)");
}

function autoMove(currentField,nextField){
    if (currentField.value.length >= currentField.maxlength){
        document.getElementById(nextField).focus();
        console.log('there');
    }
}

function blockRow(row)
{
    for (let i=0; i<row.length; i++){
        row[i].disabled=true;
    }
}

function unlockRow(row){
    for (let i=0; i<row.length; i++){
        row[i].disabled=false;
    }
}

function checkIfTheWordExists(word){
    let wordsList = ['blast','trust'];

    if (wordsList.includes(word)){
        console.log("The word is in the list");
        return true;
    }
    else{
        console.log("The word is not in the list");
        return false;
    }

}

function checkIfRowEmpty(row){
    for (let i=0; i<row.length; i++){
        if (!row[i].value){
            console.log('row is empty')
            return true;

        }
    }
    console.log("row is full")
    return false;
}
function wordInTheRow(row){
    let res = ''
    for (let i=0; i<row.length; i++){
        res+=row[i].value;
    }
    console.log('word in the row: '+ res);

    return res;


}

function checkLetters(word,wordToGuess){
    let lettersStatus=[0,0,0,0,0];  //0 - not in the word, 1 - in the word, wrong spot, 2 - in the word, correct spot
    for (let i=0; i<word.length; i++){
        if (wordToGuess[i]===word[i]){
            lettersStatus[i]=2;
        }
        else if (wordToGuess.includes(word[i])){
            lettersStatus[i]=1;
        }
    }
    console.log(lettersStatus);
}

function wordlepl()
{
    let stage=0;
    let wordToGuess = 'blast';

    console.log("Starting wordlepl game..");
    rowList = [document.getElementsByClassName('tile_input_r1'),
        document.getElementsByClassName('tile_input_r2'),
        document.getElementsByClassName('tile_input_r3'),document.getElementsByClassName('tile_input_r4'),
        document.getElementsByClassName('tile_input_r5'),document.getElementsByClassName('tile_input_r6')];
    rowStatus = [0,0,0,0,0,0];

    for (let i=1; i<rowList.length; i++){
        blockRow(rowList[i]);
    }
    let isEmpty = checkIfRowEmpty(rowList[stage]);

    if (isEmpty === false){
        let word = wordInTheRow(rowList[stage]);

        let wordExists = checkIfTheWordExists(word);

        if (wordExists===true){
            checkLetters(word,wordToGuess);
        }
    }



}




    // row = document.getElementsByClassName("tile_input_r1");
    // let i=1;
    // let check1 = false;
    // while (i<=10) {
    //     {#task(i);#}
    //     checkRow(row,i);
    //     i+=1;
    //     if (check1===true){
    //         break;
    //     }
    //  }
    //  test();

    function task(i) {
      setTimeout(function() {
          console.log(i);
      }, 2000 * i);
    }

    function checkRow(row,i){
        setTimeout(function() {
            for (let i = 0; i < row.length; i++) {
                if (!row[i].value){
                    continue;
                    check1=false;



                }
                else{
                    check1=true;
                }


        }
             console.log(check1);
        },2000*i);

    }

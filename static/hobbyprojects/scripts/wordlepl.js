function test()
{
    let res = document.getElementById('row0_res');
    let row1 = document.getElementsByClassName('tile_input_r1');
    for(let i=0; i<row1.length; i++)
    {
        res.value+=row1[i].value.toUpperCase();
    }
    console.log(":)")



}

function blockRow(row)
{
    document.getElementsByClassName(row).disabled=true;
}

function wordlepl()
{
    rowList = [document.getElementsByClassName('tile_input_r1'),
        document.getElementsByClassName('tile_input_r2'),document.getElementsByClassName('tile_input_r2'),
        document.getElementsByClassName('tile_input_r3'),document.getElementsByClassName('tile_input_r4'),
        document.getElementsByClassName('tile_input_r5'),document.getElementsByClassName('tile_input_6')]

    for (let i=1; i<rowList.length; i++){
        blockRow(rowList[i]);
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

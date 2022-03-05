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
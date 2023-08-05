const btn_cs = document.getElementById('btn_comming_soon'); // 클릭할 버튼요소를 변수 처리
const btn_Close = document.getElementById('btn_popup_close');

btn_cs.addEventListener('click', () => {
    //console.log('ldfjslkfjs');
    document.getElementById('pop_info_1').style.display = '';
});

btn_Close.addEventListener('click', () => {
    document.getElementById('pop_info_1').style.display = 'None';
});
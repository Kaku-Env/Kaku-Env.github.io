//single-contentを記事のクラスとし、記事内のh2、h3のみ取得
const headingContents = document.querySelectorAll(
    '.frame-article-middle h2')

//各見出しの絶対位置
let headingPos =  [...headingContents].map(
    element => Math.floor(element.getBoundingClientRect().top + 
    window.scrollY))

//サイド目次
const sideIndex = document.getElementById('article-index')
//サイド目次の全見出しタイトル
const sideIndexItem = sideIndex.querySelectorAll('a[href]')
//見出しの数
const headingNum = headingContents.length
//オフセット
const offset = 300

window.addEventListener('scroll', () => {
    const currentPos = window.scrollY // 現在値
    //現在値の判定
    //見出しiの位置＜スクロール量＜見出しi+1のとき、見出しiにcurrentクラスをつける
    for (let i = 0; i < headingNum; i++) {
        if (i < headingNum - 1 && currentPos + offset >= headingPos[i] && currentPos + offset < headingPos[i + 1]) {
          sideIndexItem[i].classList.add('current')
        } else if (i === headingNum - 1 && currentPos + offset >= headingPos[i]) {
          sideIndexItem[i].classList.add('current')
        } else {
            sideIndexItem[i].classList.remove('current')
        }
      }
})
const articleHearts = document.querySelectorAll(".like-glyph");

function likeCallback(e) {
  const heart = e.target;
  mimicServerCall("bogusUrl")
    .then(function(){
      if ( heart.innerText === EMPTY_HEART) {
        heart.innerText = FULL_HEART;
        heart.className = "activated-heart";
      } else {
        heart.innerText = EMPTY_HEART;
        heart.className = "";
      }
    })
    .catch(function(error) {
      const modal = document.getElementById("modal");
      modal.className = "";
      modal.innerText = error;
      setTimeout(() =>  modal.className = "hidden", 3000);
    });
}

for (const glyph of articleHearts) {
  glyph.addEventListener("click", likeCallback);
}
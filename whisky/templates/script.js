const navigation_items_elms = document.querySelectorAll(
  ".navigation-bar .list-items .item"
);
const navigation_pointer = document.querySelector(".navigation-bar .pointer");

navigation_items_elms.forEach((item, index) => {
  item.addEventListener("click", (e) => {
    e.preventDefault();
    navigation_items_elms.forEach((itm) => itm.classList.remove("active"));
    item.classList.add("active");

    const parentWidth = item.parentElement.clientWidth;
    const lefPercent = (parentWidth / navigation_items_elms.length) * index;
    navigation_pointer.style.left = lefPercent + "px";
  });
});

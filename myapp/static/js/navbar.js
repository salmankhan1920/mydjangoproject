function toggleMenu() {
    const sidebar = document.querySelector('.sidebar');
    const content = document.querySelector('.content');
    if (sidebar.style.display === 'none' || sidebar.style.display === '') {
      sidebar.style.display = 'block';
      content.style.marginRight = '200px';
    } else {
      sidebar.style.display = 'none';
      content.style.marginRight = '0px';
    }
  }
  
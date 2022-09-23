
fileInput.onchange = evt => {
    const [file] = fileInput.files
    if (file) {
        css_drop_shadow.src = URL.createObjectURL(file)
    }
  }
  
// fileInput.onchange = evt => {
//     const [file] = fileInput.files
//     if (file) {
//       project_img.src = URL.createObjectURL(file)
//     }
//   }

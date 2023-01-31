function deleteStudent(studentId) {
  fetch("/delete-student", {
    method: "POST",
    body: JSON.stringify({ studentId: studentId }),
  }).then((_res) => {
    window.location.href = "/view_attendance";
  });
}
// $(document).ready(function () {

//     const contactForm = document.getElementById('contact-form');

//     contactForm.addEventListener('submit', sendMessage);

//     function sendMessage() {

//         var data = {
//             service_id: 'gmail',
//             template_id: 'TrueBrew',
//             user_id: user,
//             template_params: {
//                 'user': contactForm.user.value,
//                 'email': contactForm.email.value,
//                 'subject': contactForm.title.value,
//                 'message': contactForm.message_body.value
//             }
//         };

//         $.ajax('https://api.emailjs.com/api/v1.0/email/send', {
//             type: 'POST',
//             url: '{% url "contact" %}',
//             data: JSON.stringify(data),
//             contentType: 'application/json',
//         }).done(function () {
//             console.log('Success!');
//         }).fail(function (error) {
//             console.log('Oops... something went wrong' + JSON.stringify(error));
//         });

//         return false;

//     }

// });

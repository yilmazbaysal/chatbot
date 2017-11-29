var question_form = $('#question-form');
    question_form.submit(function () {
        $.ajax({
            type: 'POST',
            url: '/get-answer/',
            data: question_form.serialize(),
            success: function (data) {
                // Change the text in the answer area
                $('#answer-text').text(data['answer']);
            },
            error: function() {
                alert('Something went wrong!')
            }
        });
        return false;
    });
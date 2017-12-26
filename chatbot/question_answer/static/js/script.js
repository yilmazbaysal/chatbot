var question_form = $('#question-form');
    question_form.submit(function () {
        $.ajax({
            type: 'POST',
            url: '/get-answer/',
            data: question_form.serialize(),
            success: function (data) {
                // Change the text in the answer header
                $('#answer-text').html(data['answer']);

                // Change the text in the fixed question header
                $('#fixed-question-text').html(data['spell_checked_question'])

                // Change the text in the fixed answer header
                $('#fixed-answer-text').html(data['spell_checked_answer'])
            },
            error: function() {
                alert('Something went wrong!')
            }
        });
        return false;
    });
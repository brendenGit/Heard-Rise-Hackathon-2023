$(document).ready(function () {

    //selectors
    const $userInput = $('#userInput');
    const $sendForm = $("#send");
    const $chatBox = $('#chatBox');
    const $sendFormBtn = $('#sendFormBtn');


    function sendSubmission(e) {
        const userMessage = $userInput.val().trim();
        const chatMessageHTML = `
            <div class="d-flex flex-row justify-content-start mb-4 mt-4">
                <img src="/static/avatar.png" alt="avatar" style="width: 40px; height: 100%;">
                <div>
                    <p class="small p-2 ms-3 mb-1 rounded-3" style="background-color: #f5f6f7;">
                        ${userMessage}
                    </p>
                </div>
            </div>
        `;
        $chatBox.append(chatMessageHTML);

        $userInput.val('');
        $sendFormBtn.hide();
        $('#loadingIcon').show();

        return userMessage;
    }

    async function getResponse(userMessage) {
        const response = await axios.post(
            "/send", { "user_submission": userMessage });
        const chatMessageHTML = `
            <div class="d-flex flex-row justify-content-end mr-0">
                <div>
                    <p class="small p-2 me-3 mb-1 text-white rounded-3 bg-primary">
                        ${response.data.message.content}
                    </p>
                </div>
                <img src="/static/bot_avatar.png"
                    alt="avatar 1" class="ml-0" style="width: 40px; height: 100%;">
            </div>
        `;
        $chatBox.append(chatMessageHTML);

        $('#loadingIcon').hide();
        $sendFormBtn.show();
    }


    $sendForm.on('submit', function (e) {
        e.preventDefault();
        const userMessage = sendSubmission();
        getResponse(userMessage);
    });

    // Like functionality
    $('.like-button').click(function () {
        const submissionId = $(this).data('id');
        const likesCountElement = $('#likes-count-' + submissionId);
        let likes = parseInt(likesCountElement.text());

        //Simulate liking
        likes += 1;

        likesCountElement.text(likes + ' Likes');

    });

    // Generate and set random likes for each submission
    $('.likes-count').each(function () {
        const likesCountElement = $(this);
        const randomLikes = Math.floor(Math.random() * 30);
        likesCountElement.text(randomLikes + ' Likes');
    });


});
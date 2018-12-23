$(document).ready(() => {
    const form = $("#anagramsForm");
    form.submit((event) => {
        console.log("Form submitted!");
        const fullname = $("#fullname").val();
        console.log(fullname);

        $.ajax({
            type: "POST",
            url: "/generate",
            data: {fullname: fullname},
            success: (data) => {
                console.log(data);
                if(data.results !== undefined) {
                    $("#results").html(data["results"].join("<br />"));
                }
            },
        });
        event.preventDefault();
    });
});

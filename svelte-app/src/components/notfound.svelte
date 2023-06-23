<!-- component -->
<script>
    function tohomepage(){
        window.location.href = "/"
    }
</script>
<div class="lg:px-24 lg:py-24 md:py-20 md:px-44 px-4 py-24 items-center flex justify-center flex-col-reverse lg:flex-row md:gap-28 gap-16">
    <div class="xl:pt-24 w-full xl:w-1/2 relative pb-12 lg:pb-0">
        <div class="relative">
            <div class="absolute">
                <div class="">
                    <h1 class="my-2 text-gray-800 font-bold text-2xl">
                        Looks like you've found the
                        doorway to the great nothing
                    </h1>
                    <p class="my-2 text-gray-800">Sorry about that! Please visit the homepage, Idiot</p>
                    <button class="sm:w-full lg:w-auto my-2 border rounded md py-4 px-8 text-center bg-indigo-600 text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-700 focus:ring-opacity-50" on:click={tohomepage}>Take me there!</button>
                </div>
            </div>
            <div>
                <!-- svelte-ignore a11y-img-redundant-alt -->
                <img src="https://i.ibb.co/G9DC8S0/404-2.png" alt="Image"/>
            </div>
        </div>
    </div>
    <div>
        <!-- svelte-ignore a11y-missing-attribute -->
        <img src="https://i.ibb.co/ck1SGFJ/Group.png" />
    </div>
</div>
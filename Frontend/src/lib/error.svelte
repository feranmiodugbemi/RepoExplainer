
<script>
    export let errors = []
    export let showError;
    function closeLoader() {
        showError = false;
        if (browser) {
          window.location.href = '/';
        }
    }
</script>
<!-- component -->
<!-- This is an example component -->
{#if showError}
<div id="defaultModal" tabindex="-1" aria-hidden="true" >
    <style>
  
  .loader-dots div {
      animation-timing-function: cubic-bezier(0, 1, 1, 0);
  }
  .loader-dots div:nth-child(1) {
      left: 8px;
      animation: loader-dots1 0.6s infinite;
  }
  .loader-dots div:nth-child(2) {
      left: 8px;
      animation: loader-dots2 0.6s infinite;
  }
  .loader-dots div:nth-child(3) {
      left: 32px;
      animation: loader-dots2 0.6s infinite;
  }
  .loader-dots div:nth-child(4) {
      left: 56px;
      animation: loader-dots3 0.6s infinite;
  }
  @keyframes loader-dots1 {
      0% {
          transform: scale(0);
      }
      100% {
          transform: scale(1);
      }
  }
  @keyframes loader-dots3 {
      0% {
          transform: scale(1);
      }
      100% {
          transform: scale(0);
      }
  }
  @keyframes loader-dots2 {
      0% {
          transform: translate(0, 0);
      }
      100% {
          transform: translate(24px, 0);
      }
  }
  </style>
    <div  class="fixed top-0 left-0 z-50 w-screen h-screen flex items-center justify-center" style="background: rgba(0, 0, 0, 0.3);">
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
            <!-- Modal header -->
            <div class="flex items-start justify-between p-4 border-b rounded-t dark:border-gray-600">
                <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                    Terms of Service
                </h3>
                <button type="button" on:click={closeLoader} class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="defaultModal">
                    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                    <span class="sr-only">Close modal</span>
                </button>
            </div>
            <!-- Modal body -->
            <div class="p-6 space-y-6">
                {#if errors.length > 1}
                    <ul class="text-base leading-relaxed text-red-600 dark:text-red-600">
                        {#each errors as error}
                            <li>{error}</li>
                        {/each}
                    </ul>
                    {:else}
                    <p class="text-base leading-relaxed text-red-600 dark:text-red-600">{errors[0]}</p>
                {/if}
            </div>
            <!-- Modal footer -->
            <div class="flex items-center p-6 space-x-2 border-t border-gray-200 rounded-b dark:border-gray-600">
                <button data-modal-hide="defaultModal" on:click={closeLoader} type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">I accept</button>
                <button data-modal-hide="defaultModal" on:click={closeLoader} type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">Decline</button>
            </div>
        </div>
    </div>
  </div>
  {/if}

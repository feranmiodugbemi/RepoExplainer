<script>
    export let role;
    export let content;
    export let isLoading;
  </script>
  
  <div class="grid grid-cols-12 gap-y-2">
    {#if role === 'AI'}
      {#if isLoading}
        <div class="col-start-1 col-end-8 p-3 rounded-lg">
          <div class="flex flex-row items-center">
            <div class="flex items-center justify-center h-10 w-10 rounded-full bg-indigo-500 flex-shrink-0">
              {role}
            </div>
            <div class="relative ml-3 text-sm bg-white py-2 px-4 shadow rounded-xl">
              <div class="flex items-center justify-center space-x-2">
                <div class="w-4 h-4 rounded-full animate-pulse dark:bg-violet-400"></div>
                <div class="w-4 h-4 rounded-full animate-pulse dark:bg-violet-400"></div>
                <div class="w-4 h-4 rounded-full animate-pulse dark:bg-violet-400"></div>
              </div>
            </div>
          </div>
        </div>
      {:else}
        <div class="col-start-1 col-end-8 p-3 rounded-lg">
          <div class="flex flex-row items-center">
            <div class="flex items-center justify-center h-10 w-10 rounded-full bg-indigo-500 flex-shrink-0">
              {role}
            </div>
            <div class="relative ml-3 text-sm bg-white py-2 px-4 shadow rounded-xl">
              <div class="animated-text">
                {content}
              </div>
            </div>
          </div>
        </div>
      {/if}
    {:else}
      {#if content === ""}
        <div class="col-start-6 col-end-13 p-3 rounded-lg">
          <div class="flex items-center justify-start flex-row-reverse">
            <div class="flex items-center justify-center h-10 w-10 rounded-full bg-indigo-500 flex-shrink-0">
              {role}
            </div>
            <div class="relative mr-3 text-sm bg-indigo-100 py-2 px-4 shadow rounded-xl">
              <div class="flex items-center justify-center space-x-2">
                <div class="w-4 h-4 rounded-full animate-pulse dark:bg-violet-400"></div>
                <div class="w-4 h-4 rounded-full animate-pulse dark:bg-violet-400"></div>
                <div class="w-4 h-4 rounded-full animate-pulse dark:bg-violet-400"></div>
              </div>
            </div>
          </div>
        </div>
      {:else}
        <div class="col-start-6 col-end-13 p-3 rounded-lg">
          <div class="flex items-center justify-start flex-row-reverse">
            <div class="flex items-center justify-center h-10 w-10 rounded-full bg-indigo-500 flex-shrink-0">
              {role}
            </div>
            <div class="relative mr-3 text-sm bg-indigo-100 py-2 px-4 shadow rounded-xl">
              <div>
                {content}
              </div>
            </div>
          </div>
        </div>
      {/if}
    {/if}
  </div>
  
  <style>
    .animated-text {
  display: inline-block;
  opacity: 0;
  animation: text-fade-in 1s forwards;
}

@keyframes text-fade-in {
  0% {
    opacity: 0;
    transform: translateY(10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

</style>
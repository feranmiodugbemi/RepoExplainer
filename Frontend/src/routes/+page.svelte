<script>
    import Spinner from "$lib/spinner.svelte";
    import { browser } from '$app/environment';
    let isLoading = false;
    let github_url = '';
  
    async function submit() {
      isLoading = true;
      console.log(github_url)
      const response = await fetch('https://repoexplainer.onrender.com/clone', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ "github_url": github_url }),
      });
  
      const data = await response.json();
      let github_url_data = data.repo;
  
      if (github_url_data) {
        if(browser){
          window.localStorage.setItem('github_url', github_url_data);
          isLoading = false;
          window.location.href = '/ask';
        }
      }
      else if (data.error){
        alert("Can't redirect due to error")
      }
  
    }
  </script>
  
  
  <!-- component -->
  <nav class="flex justify-between px-20 py-10 items-center bg-white">
    <div class="flex items-center justify-center rounded-2xl text-indigo-700 bg-indigo-100 h-10 w-10">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path>
      </svg>
    </div>
    <div class="flex items-center">
      <div class="flex items-center space-x-2">
        <span class="font-semibold text-gray-700">Star </span>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" class="w-5 h-5 text-yellow-400 ">
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
        </svg>
        <span class="font-semibold text-gray-700"> on Github </span>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="currentColor" style="color: #333" viewBox="0 0 24 24">
          <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
        </svg>
      </div>
    </div>
  </nav>
  
  {#if isLoading}
     <Spinner/>
  {/if}
  
  <!-- Container for demo purpose -->
  <div class="container  px-6 mx-auto">
  
    <!-- Section: Design Block -->
    <section class="mb-32 text-gray-800">
      <div class="relative overflow-hidden bg-no-repeat bg-cover" style="
            background-position: 50%;
            background-image: url('https://mdbootstrap.com/img/new/textures/full/66.jpg');
            height: 300px;
          "></div>
      <div class="container text-gray-800 px-4 md:px-12">
        <div class="block rounded-lg shadow-lg py-10 md:py-12 px-4 md:px-6" style="
              margin-top: -100px;
              background: hsla(0, 0%, 100%, 0.8);
              backdrop-filter: blur(30px);
            ">
          <div class="flex flex-wrap justify-center text-center lg:text-left">
            <div class="grow-0 shrink-0 basis-auto w-full xl:w-10/12 px-6">
              <div class="grid lg:grid-cols-2 gap-x-6 items-center">
                <div class="mb-10 lg:mb-0">
                  <h2 class="text-3xl font-bold">
                    RepoGPT
                    <br />
                    <span class="text-blue-600">Ask any questions about github repos</span>
                  </h2>
                </div>
  
                <form on:submit|preventDefault={submit}>
                  <div class="mb-6 md:mb-0">
                    <div class="md:flex flex-row">
                      <input type="text" pattern=".*\.git$" bind:value={github_url} title="Please enter a value ending with '.git'" class="form-control block w-full px-4 py-2 mb-2 md:mb-0 md:mr-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding rounded-full border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" placeholder="Enter your GitHub repo link"  required/>
                      <button type="submit" class="inline-block px-7 py-3 bg-blue-600 text-white font-medium text-sm leading-snug uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out" data-mdb-ripple="true" data-mdb-ripple-color="light">
                        Ask
                      </button>
                    </div>
                  </div>
                </form>
  
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- Section: Design Block -->
    
  </div>
  <!-- Container for demo purpose -->
  
  
  
  
  
  <footer class="fixed bottom-0 left-0 z-20 w-full p-4 bg-slate-700 border-t border-gray-200 shadow md:flex md:items-center md:justify-between md:p-6 dark:bg-gray-800 dark:border-gray-600">
    <span class="flex w-fit items-center gap-2"><span class="font-semibold text-teal-50">Built with </span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" class="w-6 h-6 text-red-500">
        <path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd"></path>
      </svg><span class="font-semibold text-teal-50"> by Feranmi odugbemi, inspired by codeeves, powered by Langchain </span></span>
  </footer>
  
  
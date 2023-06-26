<script>

  import Chat from "./components/chat.svelte";
  import Notfound from "./components/notfound.svelte";

  let isLoading = false;
  let answer = "";
  let question = "";
  let github_url = localStorage.getItem("github_url");
  let chats = [
    {role: "AI", content: `Your question about ${github_url}?` },
  ];
  const id = Math.random().toString(36).substring(2, 11);

  async function answerRequest() {
    isLoading = true;
    chats.push({role: "user", content: question });

    const response = await fetch("https://repoexplainer.onrender.com/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // Add any additional headers if required
      },
      body: JSON.stringify({ 'question':question }),
    });

    const data = await response.json();
    answer = data.answer;
    chats.push({role: "AI", content: answer });

    isLoading = false;
    // Once the request is complete, you can update the `content` variable with the received text
  }

  async function newRepo(){
    const response = await fetch("https://repoexplainer.onrender.com/reset", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // Add any additional headers if required
      },
      body: JSON.stringify({ 'request':"Reset github repo"}),
    });
    let request = await response.json()
    if (request.message === "Repository data has been reset."){
      window.localStorage.clear()
      window.location.href = '/'
    }
  }

</script>


<main>
<!-- component -->
{#if (github_url === null)}
   <Notfound/>
   {:else}
   <div class="flex h-screen antialiased text-gray-800">
    <div class="flex flex-row h-full w-full overflow-x-hidden">
      <div class="flex flex-col py-8 pl-6 pr-2 w-64 bg-white flex-shrink-0">
        <div class="flex flex-row items-center justify-center h-12 w-full">
          <div
            class="flex items-center justify-center rounded-2xl text-indigo-700 bg-indigo-100 h-10 w-10"
          >
            <svg
              class="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
              ></path>
            </svg>
          </div>
          <div class="ml-2 font-bold text-2xl">RepoGPT</div>
        </div>
        <br>
        <br>
        <div class="animated-text max-w-full overflow-hidden">
          <h1 class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl">
             Ask <span class="text-blue-600 text-5xl dark:text-blue-500"> RepoGPT </span> about : 
             <small class="ml-2 font-semibold text-gray-500 dark:text-gray-400">{github_url}</small>
          </h1>
        </div> 
        <br>
        <br>
        <br>
        <button type="submit" on:click={newRepo} class="text-white text-center inline-flex items-center bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2"><svg class="inline-block w-5 h-5 mr-1 text-white"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round">  <line x1="12" y1="5" x2="12" y2="19" />  <line x1="5" y1="12" x2="19" y2="12" /></svg> New Repo</button>
      </div>
      <div class="flex flex-col flex-auto h-full p-6">
        <div
          class="flex flex-col flex-auto flex-shrink-0 rounded-2xl bg-gray-100 h-full p-4">
          <div class="flex flex-col h-full overflow-x-auto mb-4">
            <div class="flex flex-col h-full">
              {#each chats as chat}
				<Chat role={chat.role} content={chat.content} isLoading={isLoading}/>
			  {/each}
            </div>
          </div>
          <div
            class="flex flex-row items-center h-16 rounded-xl bg-white w-full px-4"
          >
            <div>
              <button
                class="flex items-center justify-center text-gray-400 hover:text-gray-600"
              >
              </button>
            </div>
            <div class="flex-grow ml-4">
              <div class="relative w-full">
                <input
                  bind:value={question}
                  type="text"
				          placeholder="Enter Your Question"
                  class="flex w-full border rounded-2xl focus:outline-none focus:border-indigo-300 pl-4 h-10"
                />
              </div>
            </div>
            <div class="ml-4">
              <button
                on:click|preventDefault={answerRequest}
                class="flex items-center justify-center bg-indigo-500 hover:bg-indigo-600 rounded-xl text-white px-4 py-1 flex-shrink-0"
              >
                <span>Send</span>
                <span class="ml-2">
                  <svg
                    class="w-4 h-4 transform rotate-45 -mt-px"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
                    ></path>
                  </svg>
                </span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}

</main>


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
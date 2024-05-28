# cf-openai-proxy

## Usage

To use this proxy, you need to have `wrangler` installed locally to deploy workers.

Follow these steps:

1. Clone this repository.

2. Run `wrangler deploy --name xxx`, where `xxx` is the name you want to give your worker.

3. Set up environment variables:
   - Run `wrangler secret put OPENAI_HOST --name xxx` to set a custom host for the OpenAI-like API.
   - Run `wrangler secret put TOKEN --name xxx` to set a fake token, which is generated for protection against leakage.
   - Run `wrangler secret put OPENAI_API_KEY --name xxx` to set your actual OpenAI API key.

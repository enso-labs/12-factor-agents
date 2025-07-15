class Story {
  title string @stream.not_null
  content string @stream.not_null
}

function WriteMeAStory(input: string) -> Story {
  client "openai/gpt-4o"
  prompt #"
    Tell me a story

    {{ ctx.output_format() }}

    {{ _.role("user") }}

    Topic: {{input}}
  "#
}

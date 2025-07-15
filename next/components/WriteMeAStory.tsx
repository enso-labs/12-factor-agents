'use client'

import { useWriteMeAStory } from "@/baml_client/react/hooks";
import { Button } from "@/components/ui/button";

export function WriteMeAStory() {
  const writeMeAStory = useWriteMeAStory({
    onStreamData: (partial) => {
      // Handle real-time updates
      console.log('Story in progress:', partial);
    },
    onFinalData: (final) => {
      // Handle completed story
      console.log('Story completed:', final);
    }
  });

  return (
    <div>
      <Button
        onClick={() => writeMeAStory.mutate("About a cat in a hat")}
        disabled={writeMeAStory.isLoading}>
        {writeMeAStory.isLoading ? 'Generating...' : 'Generate Story'}
      </Button>

      {writeMeAStory.data && (
        <div>
          <h4>{writeMeAStory.data.title}</h4>
          <p>{writeMeAStory.data.content}</p>
        </div>
      )}

      {writeMeAStory.error && <div>Error: {writeMeAStory.error.message}</div>}
    </div>
  );
}

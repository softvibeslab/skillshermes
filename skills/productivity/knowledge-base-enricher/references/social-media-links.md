# Handling Social Media Links Requiring Engagement

Some social media platforms (particularly Instagram) use engagement-gated mechanisms where:
- Content is only accessible after commenting with a specific keyword
- Links are sent via direct message rather than displayed publicly
- The actual resource URL is not visible in the post itself

## Common Patterns
- "Comment 'KEYWORD' for link" 
- "Reply with [word] to get the resource"
- "DM sent after commenting"

## Workflow for Handling Such Links
1. **Identify the mechanism**: Look for phrases indicating comment-based access
2. **Engage as instructed**: Comment the required keyword
3. **Check for response**: Monitor notifications/DMs for the reply containing the actual link
4. **Process the actual link**: Once obtained, treat it as a regular URL for knowledge capture

## Limitations of Automated Processing
- Automated tools cannot perform the required social media action (commenting)
- The actual resource URL is not present in the initial page source
- Manual intervention is required to obtain the real link

## Recommendation
When encountering such links:
1. Document the social media post and the access mechanism
2. Perform the required action manually (or have the user do it)
3. Once the actual link is obtained, use the knowledge-base-enricher skill on the real URL
4. Link your notes about the social media post to the resource notes for context

## Example Documentation Format
```markdown
# Social Media Resource: [Tool Name]

**Source:** Social media post requiring engagement
**Platform:** [Instagram/Twitter/etc.] 
**Access Mechanism:** Comment "[KEYWORD]" to receive link via DM
**Post URL:** [Social media post URL]
**Date Accessed:** [Date]

## Access Process
1. Commented "[KEYWORD]" on the post
2. Received direct message with link: [Actual URL]
3. Processed the actual URL using knowledge-base-enricher

## Notes on the Social Media Post
[Any relevant context about why this resource was shared, the author, etc.]
```
# Contributing a Guide to the Library

Made a guide with the Bible Teacher skills that you'd like to add to the shared
library? This page shows how — **from your phone, no coding and no git**.

## The easy way: just say "submit this"

Right after Claude makes a guide, type **"submit this"** (or **"commit this"**).
Claude will show the guide in a copy block and give you a **tappable GitHub link** with
everything pre-filled. Then it's two taps: **Copy** → open the link → **paste** → **Commit
changes**. That's it. (The detailed steps below are the same thing, spelled out.)

---

> **You need to be a collaborator first.** Ask Ken to add you (he does this in the
> repo's **Settings → Collaborators**). You'll get an email/notification invite —
> accept it. Use **your own** GitHub account; never ask for or share anyone else's
> password or access token.

---

## What you're doing, in one sentence

Your guide is already **one self-contained HTML file** (the skills build it that
way on purpose). You just **copy that HTML out of Claude and paste it into a new
file on GitHub.**

---

## Step by step (phone browser)

1. **Copy your guide's HTML.** In your Claude chat, find the ```html code block
   (or the artifact) and copy the whole thing. If there's a copy button, use it;
   otherwise select all the code and copy.
2. **Open the repo on GitHub.** Go to **github.com/ken-muturi/bible-teacher** and
   sign in. (If buttons are hard to tap, use your browser's **"Request desktop
   site"** option.)
3. **Pick the right folder** for your guide type:

   | Your guide | Folder |
   |------------|--------|
   | Sermon outline | `guides/sermons/` |
   | Passage study or simple one-page teaching | `guides/passages/` |
   | Book overview panel, infographic deck, or comparison | `guides/visuals/` |
   | Discussion guide | `guides/discussions/` |

4. **Add the file.** Tap **Add file → Create new file**.
5. **Name it.** Type the folder path + a short, lowercase, hyphenated name ending
   in `.html`. Example:
   `guides/sermons/communion-with-the-spirit-outline.html`
   (Typing the `guides/sermons/` part puts the file in that folder.)
6. **Paste** your HTML into the big text box.
7. **Commit.** Scroll down and tap **Commit changes**. A short message like
   "Add sermon: communion with the Spirit" is perfect.

That's it — your guide is live. Because it's self-contained, it renders on its own
at its GitHub Pages URL and as a file.

> **Prefer the GitHub mobile app?** It's great for *editing* a file you've already
> added. For *creating* a new file, the website (step 2 above) is the reliable way.

---

## A couple of things to know

- **You'll be credited automatically.** You don't need to add your name anywhere. When
  Ken runs the build, a small *"Contributed by &lt;your name&gt; · &lt;date&gt;"* line is
  added to the foot of your guide, taken from your GitHub commit. (And GitHub always
  records you as the author in the file's history and blame, regardless.) So commit from
  **your own** account — that's how you get the credit.
- **The index/gallery card is Ken's step.** New files don't automatically appear on
  the home page (`index.html`) — Ken adds the little gallery card and runs the build
  so it also picks up the shared stylesheet and your byline. Your file still works and
  renders on its own in the meantime; just tell Ken it's there.
- **Naming:** lowercase, words-separated-by-hyphens, end in `.html`. Match the style
  of the files already in the folder.
- **One guide per file.** Keep each teaching, outline, or deck in its own file.

---

## If direct editing ever gets turned off

If Ken later turns on review (branch protection), the only change is: when you
**Commit changes**, choose **"Create a new branch and start a pull request"** instead
of committing straight to `main`. Ken then approves it with one tap. Everything else
is the same.

---

## Security — please read

- Use **your own** GitHub account. Never share Ken's password or a personal access
  token, and never paste credentials into a Claude chat or a guide.
- Only add Bible-teaching guides you made with the toolkit. Don't paste anything
  with personal data, passwords, or keys in it.
